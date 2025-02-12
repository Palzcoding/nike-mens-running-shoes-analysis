# **Nike Men's Running Shoes Data Analysis**

## **Project Overview**
This personal project analyzes data scraped from Nike's official website, focusing on men's running shoes. The dataset includes various product attributes on the website. 
I started this project in interest of boosting my data analysis skill and extract useful information to help myself picking Nike running shoes.

Tools: Python(pandas, seaborn, numpy), Website Scraping

---

## **Data Collection**
The dataset was obtained through web scraping, targeting Nike's men's running shoe listings. The collected data contains:

- **Product Name**
- **Current Price**
- **Full Price**: The original price
- **Discount**: The percentage discount applied to the product in %.
- **Frequency of Appearance**: Some products appear multiple times due to small variations of designs.

The dataset contains **198 entries**, with some duplicated listings due to Nike’s own structuring of its products on website.

The data collection process strictly follows Nike's robots.txt.

---

## **Data Analysis & Insights**

### **1. Most Frequent Products**
The products Nike prioritizes in quantity showing on their platform. 
The top three are AIR ZOOMFLY VOMERO 17, NIKE INFINITY RN 4, and NIKE ALPHAFLY 3 
By Nike's default listing, frequent products appear on both top page and bottom page, potentially due to **marketing strategies**.

### **2. Price Distribution**
A **histogram analysis of product prices** is created to show Nike's pricing strategy of different models in the market. 
The two most concentrated pricing points are $105 nd $180. The whole range is from $50 to %285, with no price located in $190 - $250.  
The pricing are very dense in the range below $100. Nike is trying to offer a wide-range of affordable options.

### **3. Discount Trends**
The **discount percentages** are calculated across different products. Nike is willing to offer three products significant discounts while complete 0 discount for others.
The discount are for low-popularity colored shoes and legacy running shoes. A time-series data will better explain.

### **4. Price Sensitivity Analysis**
Nike's pricing strategy for men's running shoes demonstrates low price elasticity. The majority of products maintaining no discounts (0-5%). Significant markdowns (30-35%) are concentrated in the $100-$150 range. The mid-tier models are discounted for inventory turnover. High-level professional models ($200+) are prized stably. There'ss strong demand without price incentives. 
The rarity of discounts indicates Nike’s aproach to preserve shoes values.

---

## **Implications**
Nike’s Pricing Strategy can be seen through the analyzing of price ranges and discount. From the marketing positioning of a leader sports company we can learn. 

The frequently listed products indicate consumer demand.

Also useful for Shoppers like me to determine best time and product to buy. 

---

## **Potential improvement**
Future improvements could include:

- Expanding the dataset to include **more categories** or a longer time period to capture pricing fluctuations.
- Using "word cloud analysis" to find relationship between features and prices, or features and customer ratings.
    Dynamic Javascript Loading make it hard to extract text data from descriptions. The major part of data for the project are in json form. Selenium will be learned in the future


---

## ** KEEP MOVING FORWARD !! **
