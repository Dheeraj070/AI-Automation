import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_brand_performance(df):
    df['Brand'] = df['Brand'].fillna('').str.strip()
    df = df[df['Brand'] != '']

    brand_counts = df['Brand'].value_counts().head(5)
    if brand_counts.empty:
        print("[!] No brand data available to plot.")
        return

    avg_rating_by_brand = df.groupby('Brand')['Rating'].mean().sort_values(ascending=False).head(5)

    # Bar chart: Top 5 brands
    brand_counts.plot(kind='bar', title="Top 5 Brands by Frequency", color='skyblue')
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("top_brands_bar.png")
    plt.clf()

    # Pie chart: Brand share
    brand_counts.plot(kind='pie', autopct='%1.1f%%', title="Top 5 Brand Share")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("top_brands_pie.png")
    plt.clf()


def price_vs_rating(df):
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df['Selling Price'] = pd.to_numeric(df['Selling Price'], errors='coerce')
    df = df.dropna(subset=['Rating', 'Selling Price'])

    # Scatter plot
    sns.scatterplot(x='Rating', y='Selling Price', data=df)
    plt.title("Price vs Rating")
    plt.xlabel("Rating")
    plt.ylabel("Price (INR)")
    plt.tight_layout()
    plt.savefig("price_vs_rating_scatter.png")
    plt.clf()

    # Average price by rating
    rating_bins = pd.cut(df['Rating'], bins=[0, 2, 3, 4, 5], labels=['0-2', '2-3', '3-4', '4-5'])
    avg_price = df.groupby(rating_bins, observed=False)['Selling Price'].mean()
    avg_price.plot(kind='bar', title="Avg Price by Rating Range", color='green')
    plt.ylabel("Average Price (INR)")
    plt.tight_layout()
    plt.savefig("avg_price_by_rating.png")
    plt.clf()


def review_rating_distribution(df):
    df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

    # Top 5 by reviews
    top_reviews = df.dropna(subset=['Reviews']).sort_values(by='Reviews', ascending=False).head(5)
    sns.barplot(x='Title', y='Reviews', data=top_reviews)
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 5 Products by Reviews")
    plt.tight_layout()
    plt.savefig("top_reviews_bar.png")
    plt.clf()

    # Top 5 by rating
    top_rated = df.dropna(subset=['Rating']).sort_values(by='Rating', ascending=False).head(5)
    sns.barplot(x='Title', y='Rating', data=top_rated)
    plt.xticks(rotation=45, ha='right')
    plt.title("Top 5 Products by Rating")
    plt.tight_layout()
    plt.savefig("top_rated_bar.png")
    plt.clf()


# Main function to run all analyses
def run_analysis():
    df = pd.read_csv("cleaned_soft_toys.csv")
    analyze_brand_performance(df)
    price_vs_rating(df)
    review_rating_distribution(df)
    print("[✓] Analysis and plots completed.")

run_analysis()
