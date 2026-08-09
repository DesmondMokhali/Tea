# Earth Inventory - Design System & Standards

This document outlines the core design tokens, typography, colors, and UI principles for **Earth Inventory** (formerly The Herbalist). It serves as the single source of truth for the brand's look and feel to ensure consistency across all web pages and components.

## Brand Identity
- **Name**: Earth Inventory
- **Slogan**: Traditional Chinese Wellness
- **Aesthetic**: Premium, sophisticated, natural, and apothecary-inspired. The design should evoke trust, heritage, and scientific efficacy.

## 1. Typography

The typography system uses a mix of elegant serifs for branding and headings, and clean sans-serifs for readability in body text and UI elements.

- **Brand Logo & Primary Headings**: `Cormorant Garamond` (Weights: 400, 500, 600, 700)
- **Secondary Headings & Accents**: `Playfair Display` (Weights: 400, 600, 700)
- **Body Text**: `DM Sans` (Weights: 300, 400, 500, 600)
- **Buttons & Small UI Labels**: `Montserrat` (Weights: 600, 700, 800)

## 2. Color Palette

The color palette is rooted in nature, using deep forest greens, warm apothecary golds, and parchment creams.

### Backgrounds
- **Primary Cream (Page Background)**: `#f6f2e6` (CSS Var: `--c`)
- **Secondary Cream (Cards/Surfaces)**: `#e8e0cc` (CSS Var: `--cd`)
- **White (Clean Surfaces)**: `#ffffff`

### Primary Brand (Greens)
- **Forest Green (Dark, Headers, Footer)**: `#1b3a28` (CSS Var: `--f`)
- **Muted Forest**: `#2a5040` (CSS Var: `--fm`)
- **Light Forest**: `#3a6852` (CSS Var: `--fl`)

### Accents (Golds & Sage)
- **Primary Gold (Buttons, Highlights)**: `#c8a06e` (CSS Var: `--g`)
- **Light Gold (Hover states, text accents)**: `#dab882` (CSS Var: `--gl`)
- **Pale Gold**: `#f0e0c4` (CSS Var: `--gp`)
- **Sage Green (Success, secondary accents)**: `#6a9970` (CSS Var: `--s`)
- **Light Sage**: `#9abf9d` (CSS Var: `--sl`)

### Text Colors
- **Dark Text (Primary)**: `#182415` (CSS Var: `--t`)
- **Medium Text (Secondary)**: `#3d5c44` (CSS Var: `--tm`)
- **Light Text (Muted/Placeholders)**: `#7a9280` (CSS Var: `--tl`)

## 3. Shadows & Elevation

Shadows are soft, tinted with the primary forest green to avoid harsh black drop-shadows, creating a more integrated, premium feel.

- **Base Shadow (`--sh0`)**: `0 2px 12px rgba(27, 58, 40, 0.07)`
- **Medium Shadow (`--sh1`)**: `0 4px 28px rgba(27, 58, 40, 0.13)` (Used for hovering over cards)
- **Large Shadow (`--sh2`)**: `0 12px 56px rgba(27, 58, 40, 0.20)` (Used for modals and floating elements)

## 4. UI Elements

### Buttons
- **Primary**: Background `#c8a06e`, Text `#1b3a28`. Font: Montserrat bold.
- **Secondary**: Background `#1b3a28`, Text `#c8a06e`. Font: Montserrat bold.
- **Border Radius (`--r`)**: Standardized at `12px` for a soft, modern feel.

### Logo
- Uses the custom SVG `ei_logo_e2dbc7.svg`.
- The logo mark color is specifically `#e2dbc7` to match the cream/beige aesthetic when placed on dark header backgrounds.

### Layout & Borders
- **Transitions (`--tr`)**: Smooth animations using `0.24s cubic-bezier(0.4, 0, 0.2, 1)`.
- **Top Utility Bar**: Very dark green (`#112519`), slim (32px), used for secondary links and shipping notices.
- **Main Header**: Sticky top, dark forest (`#1b3a28`), with subtle white-alpha borders (`rgba(255,255,255,0.1)`).

## 5. Trust Bar
A standard Trust Bar is used across product and collection pages to reinforce brand promises.
- **Background**: `#e8e0cc` (Dark Cream)
- **Icons**: Lucide icons in Gold (`#c8a06e`) and Sage (`#6a9970`).
- **Items**: 
  - 100% Natural Herbs
  - Specialist Formulated
  - FREE Courier Delivery
  - Scientifically Researched
