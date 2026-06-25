import { useState, useEffect } from 'react';

/**
 * Custom React hook for fetching and enriching product data from Google Drive endpoints.
 * @param {Object} endpoints - The endpoints for product catalog, inventory ledger, and product reviews.
 * @returns {Object} { products, loading, error, getProductReviews }
 */
export function useProductData(endpoints) {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [rawReviews, setRawReviews] = useState([]);

  useEffect(() => {
    let isMounted = true;

    async function fetchData() {
      try {
        setLoading(true);
        // Concurrent async/await fetch operations
        const [catalogRes, inventoryRes, reviewsRes] = await Promise.all([
          fetch(endpoints.catalog).then((r) => r.json()),
          fetch(endpoints.inventory).then((r) => r.json()),
          fetch(endpoints.reviews).then((r) => r.json()),
        ]);

        if (!isMounted) return;

        // Save raw reviews for helper utilities
        setRawReviews(reviewsRes);

        // Map inventory lookup by External ID
        const inventoryMap = {};
        inventoryRes.forEach((item) => {
          if (item.external_id) {
            inventoryMap[item.external_id.trim()] = item.quantity;
          }
        });

        // Enrich catalog products with calculated Stock Status
        const enrichedProducts = catalogRes.map((product) => {
          const extId = product.external_id ? product.external_id.trim() : '';
          const quantity = inventoryMap[extId] !== undefined ? inventoryMap[extId] : 0;

          let stockStatus = 'Out of Stock';
          if (quantity > 10) {
            stockStatus = 'In Stock';
          } else if (quantity > 0) {
            stockStatus = 'Low Stock';
          }

          return {
            ...product,
            quantity,
            stockStatus,
            isOutOfStock: stockStatus === 'Out of Stock',
          };
        });

        setProducts(enrichedProducts);
        setError(null);
      } catch (err) {
        if (isMounted) {
          setError(err.message || 'Failed to fetch product datasets');
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    if (endpoints && endpoints.catalog && endpoints.inventory && endpoints.reviews) {
      fetchData();
    }

    return () => {
      isMounted = false;
    };
  }, [endpoints]);

  /**
   * Helper function to extract targeted reviews and calculated average star rating.
   * @param {string} externalId - Zero-padded unique External ID of the product.
   * @returns {Object} { reviews: Array, averageRating: number }
   */
  const getProductReviews = (externalId) => {
    if (!externalId) return { reviews: [], averageRating: 0 };
    const filtered = rawReviews.filter(
      (rev) => rev.external_id && rev.external_id.trim() === externalId.trim()
    );

    if (filtered.length === 0) {
      return { reviews: [], averageRating: 0 };
    }

    const totalStars = filtered.reduce((sum, rev) => sum + (Number(rev.rating) || 0), 0);
    const averageRating = parseFloat((totalStars / filtered.length).toFixed(1));

    return {
      reviews: filtered,
      averageRating,
    };
  };

  return { products, loading, error, getProductReviews };
}
