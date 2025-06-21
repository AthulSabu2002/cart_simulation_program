# 🛒 Product Catalogue & Discount Calculation Program

This program simulates a basic checkout system with a product catalogue and a set of discount rules. It prompts the user for product quantities and gift wrapping options, then calculates the total cost with the most beneficial discount applied.

---

## 📦 Product Catalogue

| Product     | Price |
|-------------|-------|
| Product A   | $20   |
| Product B   | $40   |
| Product C   | $50   |

---

## 🎁 Discount Rules

Only **one** discount can be applied per purchase — the one that offers the **maximum savings**.

1. **flat_10_discount**  
   → Applies a **flat $10 discount** if the cart total exceeds **$200**.

2. **bulk_5_discount**  
   → Applies a **5% discount** on a product’s total if **more than 10 units** of that product are purchased.

3. **bulk_10_discount**  
   → Applies a **10% discount on the entire cart** if **total quantity** across all products exceeds **20 units**.

4. **tiered_50_discount**  
   → Applies a **50% discount** on units **beyond 15** of any product **if total quantity exceeds 30 units**.  
     - First 15 units are charged at full price.
     - Remaining units (above 15) of that product get a 50% discount.

---

## 💡 How It Works

1. User inputs:
   - Quantity for each product.
   - Whether each product is gift-wrapped.

2. Output displayed:
   - Each product’s name, quantity, and total cost.
   - Cart **subtotal**.
   - **Best applicable discount name** and **discount amount**.
   - Final **total payable** after discount.

---

