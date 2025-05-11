import pandas as pd

def clean_data(file_path="sponsored_soft_toys.csv"):
    df = pd.read_csv(file_path)

    # Remove duplicates
    df.drop_duplicates(subset=["Product URL"], inplace=True)

    # Clean price 
    df['Selling Price'] = df['Selling Price'].astype(str).str.replace(',', '', regex=False).str.replace('₹', '', regex=False)
    df['Selling Price'] = pd.to_numeric(df['Selling Price'], errors='coerce')

    # Clean ratings and reviews
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

    # Drop rows with missing critical values
    df.dropna(subset=['Selling Price', 'Rating', 'Reviews'], inplace=True)

    df.to_csv("cleaned_soft_toys.csv", index=False)
    return df

df_clean = clean_data()
