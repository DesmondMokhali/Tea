/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        forest: {
          50:  '#eef4f0',
          100: '#d5e8da',
          200: '#aad0b6',
          500: '#2d7a50',
          700: '#1b3a28',
          800: '#132b1e',
          900: '#0d1f15',
        },
        sage: {
          100: '#dff0e6',
          200: '#b8d9c4',
          400: '#6ab08a',
          500: '#4a9b6f',
          600: '#3a7d58',
        },
        cream: {
          50:  '#faf8f5',
          100: '#f2ede6',
          200: '#e8dfd4',
        },
        amber: {
          50:  '#fffbeb',
          100: '#fef3c7',
          400: '#fbbf24',
          500: '#f59e0b',
        },
      },
      fontFamily: {
        display: ['"Playfair Display"', 'Georgia', 'serif'],
        sans:    ['"DM Sans"', '"Inter"', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        card:  '0 2px 12px rgba(27,58,40,0.08)',
        hover: '0 6px 24px rgba(27,58,40,0.14)',
      },
    },
  },
  plugins: [],
}
