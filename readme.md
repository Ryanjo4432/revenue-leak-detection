# Revenue Leak Detection in E-Commerce

Identifying where and why an e-commerce business loses money — using real transactional data, SQL analysis, and Python visualizations.

---

## 🧩 Problem

Businesses often generate strong revenue on paper but still lose profit through cancellations, high shipping costs, poor customer retention, and over-reliance on a small set of products. This project identifies those exact leaks using data.

---

## 📦 Dataset

**Brazilian E-Commerce Public Dataset by Olist**
- Source: [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- 100,000+ orders from 2016–2018
- 8 relational tables: customers, orders, products, sellers, payments, reviews, geolocation

---

## ⚙️ Tech Stack

| Tool       | Purpose                        |
|------------|--------------------------------|
| Python     | Data cleaning & analysis       |
| Pandas     | Data manipulation              |
| PostgreSQL | Relational database & queries  |
| Matplotlib | Visualizations                 |
| Seaborn    | Statistical charts             |
| Jupyter    | Interactive analysis notebook  |

---

## 🏗️ Project Structure

```
revenue-leak-detection/
│
├── data/
│   ├── raw/          ← original CSVs (not tracked in git)
│   └── cleaned/      ← cleaned CSVs (not tracked in git)
│
├── notebooks/
│   └── analysis.ipynb
│
├── sql/
│   ├── schema.sql    ← table definitions with foreign keys
│   └── queries.sql   ← analysis queries
│
├── src/
│   ├── db_connection.py
│   ├── clean_data.py
│   └── load_data.py
│
├── visuals/          ← all charts saved here
├── README.md
└── requirements.txt
```

---

## 🔍 Key Findings

### 1. 80/20 Rule — Product Revenue Concentration
- **Top 26% of products generate 80% of total revenue**
- Bottom 20% of products average only **R$31 revenue each**
- Total revenue analyzed: **R$13,406,593**
- → *Focus inventory and marketing on top-performing products*

### 2. Customer Segmentation (RFM Analysis)
- **At Risk customers hold R$2.8M** — the single biggest danger to revenue
- **27,534 customers need attention** — largest group being ignored
- Champions (top spenders) average **R$275 per order** — highest value segment
- **R$532,320 already lost** to completely inactive customers
- → *Re-engagement campaigns for At Risk segment could recover millions*

### 3. Cancellation Loss
- **R$97,242 lost** to cancelled and unavailable orders
- 461 cancelled orders averaging **R$206 each**
- → *Improving stock availability could directly recover this revenue*

### 4. Late Delivery Impact on Reviews
- Orders with **1-star reviews** arrived on average **3.3 days late**
- Orders with **5-star reviews** arrived on average **12.7 days early**
- Clear correlation: **every day late = lower review score**
- → *Faster delivery directly drives customer satisfaction and repeat purchases*

### 5. Freight as a Revenue Leak
- **All top 15 categories exceed the 20% freight threshold**
- `signaling_and_security` spends **30.26%** of revenue on freight
- `food_drink` and `electronics` both above **29%**
- → *These categories need renegotiated shipping rates or pricing adjustments*

---

## 💡 Business Recommendations

1. **Protect Champions** — loyalty rewards for top 6,449 customers spending R$275+ avg
2. **Re-engage At Risk segment** — R$2.8M at stake, target with win-back campaigns
3. **Cut underperforming products** — bottom 20% generate almost no revenue
4. **Negotiate freight for furniture & electronics** — shipping eating 25-30% of revenue
5. **Improve delivery speed** — direct impact on reviews, retention, and repeat orders
6. **Reduce cancellations** — better stock management recovers R$97K immediately

---

## 📊 Visualizations

| Chart | Insight |
|-------|---------|
| Pareto Chart | Top 26% products = 80% revenue |
| RFM Segments | Customer value distribution |
| Freight Leak | Categories losing margin to shipping |
| Late Delivery | Delivery speed vs review score |
| Cancellation Loss | Revenue lost by order status |
| Monthly Trend | Revenue growth over time 