
import pandas as pd
from langchain_core.documents import Document


def dataconveter():
    product_data=pd.read_csv("../data/amazon_product_review.csv")

    data=product_data[["product_title","Text"]]

    product_list = []

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        # Construct an object with 'product_name' and 'review' attributes
        obj = {
                'product_ID': row['ProductId'],
                'review': row['Text']
            }
        # Append the object to the list
        product_list.append(obj)

        
            
    docs = []
    for entry in product_list:
        metadata = {"product_ID": entry['product_ID']}
        doc = Document(page_content=entry['review'], metadata=metadata)
        docs.append(doc)
    return docs