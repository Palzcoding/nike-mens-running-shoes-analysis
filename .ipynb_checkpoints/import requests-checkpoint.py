{"experienceProducts":[{"cloudProductId":"2035f4a6-e459-503e-86e1-aa27bf9c2dfe","currentPrice":140},{"cloudProductId":"ddf015d7-918c-5d8d-ae7f-490b62c64623","currentPrice":210},{"cloudProductId":"52570333-3b54-54ae-8688-6744994f9f20","currentPrice":180},{"cloudProductId":"3672e96a-d61a-5bd4-aef7-7635102b2bff","currentPrice":170},{"cloudProductId":"81ff8440-c4a8-5376-8dc8-0ae19d06855c","currentPrice":150},{"cloudProductId":"d72f9e08-8129-5d8a-9a8f-d30b0999b23b","currentPrice":160},{"cloudProductId":"22133469-bb98-5e09-bd1e-2da07349f8c9","currentPrice":140},{"cloudProductId":"688520d7-02df-55e6-945e-7cf6b284471d","currentPrice":140},{"cloudProductId":"60d15bd3-752a-589d-ab1e-bfcfb26e9cd8","currentPrice":119.97},{"cloudProductId":"187f60ab-efe8-5fd4-8611-c2061b5f4411","currentPrice":140},{"cloudProductId":"392762c9-1603-584c-8674-87a9723bba4c","currentPrice":0}],"country":"us"}

import requests
import json

# Successfully Obtained Sample Pegasus 41
# Nike Official API
nike_api_url = "https://product-proxy-v2.adtech-prod.nikecloud.com/products"

# Request headers
headers = {
    "Content-Type": "application/json",
    "Origin": "https://www.nike.com",
    "Referer": "https://www.nike.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Request body (Payload)
data = {
    "experienceProducts": [
        {"cloudProductId": "0196c7a7-a5b1-5f72-a4e2-b939bd771666", "currentPrice": 140},
        {"cloudProductId": "e9fca3fa-2661-587b-9371-d0fdb83611fe", "currentPrice": 180},
        {"cloudProductId": "0725626c-44b2-51f1-9d51-ed141d320c9e", "currentPrice": 170},
        {"cloudProductId": "5434425a-dadb-5139-a111-7e9245127d03", "currentPrice": 140},
        {"cloudProductId": "1adfc052-5bbe-59cd-b274-e3277abdd744", "currentPrice": 103.97},
        {"cloudProductId": "5fa03ccd-bbae-5307-b66a-a920b9268581", "currentPrice": 103.97},
        {"cloudProductId": "aaf169ae-a9fc-5eb3-9e73-79550529e2f8", "currentPrice": 180},
        {"cloudProductId": "ddf015d7-918c-5d8d-ae7f-490b62c64623", "currentPrice": 210},
        {"cloudProductId": "8f5894d9-b60b-54aa-b24c-4e21e1e327dc", "currentPrice": 285},
        {"cloudProductId": "469b0711-ab00-5db2-b3bb-7f4b8ffd3d69", "currentPrice": 260},
        {"cloudProductId": "44cd70c0-3d0a-59a7-aef2-1a6e3c6266c1", "currentPrice": 90},
        {"cloudProductId": "6de7ff29-0eb0-53fa-8467-c07763a96e9a", "currentPrice": 170},
        {"cloudProductId": "81ff8440-c4a8-5376-8dc8-0ae19d06855c", "currentPrice": 150},
        {"cloudProductId": "e8d33dae-9c06-5481-8ee2-b1b6ea458465", "currentPrice": 180},
        {"cloudProductId": "b8e7a3f8-ed29-5b22-9669-fa3b6dc93919", "currentPrice": 190},
        {"cloudProductId": "0a3dc689-3bf8-5842-94e0-eb9226ac2bee", "currentPrice": 160},
        {"cloudProductId": "495c5509-7bf4-52cf-ab0f-dfc9185aa0f3", "currentPrice": 190},
        {"cloudProductId": "fb31ea37-2e22-5eeb-b208-293e24eeac34", "currentPrice": 190},
        {"cloudProductId": "653f0964-5524-516d-a7e4-a008a1a488ad", "currentPrice": 75},
        {"cloudProductId": "0da4d244-63f1-53ad-ace5-8b935a567bf4", "currentPrice": 100},
        {"cloudProductId": "da477238-d164-5a72-8198-d66e41bf6fbf", "currentPrice": 89.97},
        {"cloudProductId": "20b4b03b-32fe-57b8-bb13-c43cac7c6c7c", "currentPrice": 79.97},
        {"cloudProductId": "d72f9e08-8129-5d8a-9a8f-d30b0999b23b", "currentPrice": 160},
        {"cloudProductId": "74614a1c-2600-5c00-a958-0fdc3967defc", "currentPrice": 130},
        {"cloudProductId":"aaf169ae-a9fc-5eb3-9e73-79550529e2f8","currentPrice":180},
        {"cloudProductId":"5dbe1065-e4b3-5434-899a-ea5a3c9d2002","currentPrice":125.97},
        {"cloudProductId":"469b0711-ab00-5db2-b3bb-7f4b8ffd3d69","currentPrice":260},
        {"cloudProductId":"1adfc052-5bbe-59cd-b274-e3277abdd744","currentPrice":103.97},
        {"cloudProductId":"62174ac8-b9cf-5bc7-8541-98f52341fc56","currentPrice":103.97},
        {"cloudProductId":"fb807d6f-f148-583e-b08d-09e614c9b3a6","currentPrice":275},
        {"cloudProductId":"a6396e78-c418-5799-affe-fc6174b5b386","currentPrice":116.97},
        {"cloudProductId": "0725626c-44b2-51f1-9d51-ed141d320c9e", "currentPrice": 170},
        {"cloudProductId": "863cec79-eeb3-56f0-b6a3-e360596ea264", "currentPrice": 320},
        {"cloudProductId":"5434425a-dadb-5139-a111-7e9245127d03","currentPrice":140},
        {"cloudProductId":"16a0c2df-4e79-57e4-826c-28e9eff4e329","currentPrice":97.97},
        {"cloudProductId":"bfab83b5-4af6-5485-a465-3c6e77fbbdc6","currentPrice":55.97},
        {"cloudProductId":"de0ea368-8d70-5ae5-bea7-38765a10a749","currentPrice":51.97},
        {"cloudProductId":"138c07c7-ce72-5085-a09b-3d171b0e9c88","currentPrice":90},
        {"cloudProductId":"2c460604-2080-57c2-a99b-f16a27134f77","currentPrice":80},
        {"cloudProductId":"c559971a-0b6a-5dd9-816b-849557110825","currentPrice":140},
        {"cloudProductId":"5c0e64ac-62f6-57ae-a980-7bfa1e9354d8","currentPrice":70},
        {"cloudProductId":"4634c4bc-b959-5133-ae61-7d2335a69fde","currentPrice":48.97},
        {"cloudProductId":"0424f526-c376-5940-8bb0-52b4e6f36f77","currentPrice":70},
        {"cloudProductId":"83bba6e0-d5b9-5ccf-9c79-1ac112ad528c","currentPrice":85},
        {"cloudProductId":"03e99200-b528-5db8-91c8-6ccd6ea5db77","currentPrice":55.97},
        {"cloudProductId":"37bd2dbf-9f86-5076-aa41-1cf31cba62d9","currentPrice":48.97},
        {"cloudProductId":"9c96e37c-1b4e-5278-8088-bf6463b8dac4","currentPrice":44.97},
        {"cloudProductId":"d22ed536-45af-5708-96ac-60af33426924","currentPrice":84.97},
        {"cloudProductId":"85d12450-7c8d-5acb-b105-4d25cd2573a8","currentPrice":58.97},
        {"cloudProductId":"0b6eca36-76ab-5be1-a3cf-8554cd1abedb","currentPrice":30},
        {"cloudProductId":"94e5b117-0501-590b-a5ab-f6f9d3e061a7","currentPrice":30},
        {"cloudProductId":"711b255d-e70a-5602-bee2-6e231151f6ee","currentPrice":115},
        {"cloudProductId":"adbac3d6-a598-5ba4-8cde-d0318dc744ae","currentPrice":30},
        {"cloudProductId": "47778c24-465b-51aa-a95d-90aa7e447011", "currentPrice": 103.97},
        {"cloudProductId": "da477238-d164-5a72-8198-d66e41bf6fbf", "currentPrice": 89.97},
        {"cloudProductId": "3b4e32f6-57b4-53ee-9429-1eb97e137134", "currentPrice": 79.97},
        {"cloudProductId":"217d7abe-d84c-589f-b4f1-a1b8c9665544","currentPrice":97.97},
        {"cloudProductId":"90b9fef1-7b3e-51f4-96d9-47dbb7b2f249","currentPrice":125.97}
    ], 
    "country": "us"
}

# Send the request
response = requests.post(nike_api_url, headers=headers, data=json.dumps(data))

# Check the response status code
if response.status_code == 200:
    nike_data = response.json()
    print("Data successfully retrieved!")
    print(nike_data)  # Parse JSON data
else:
    print(f"Request failed, status code: {response.status_code}, error message: {response.text}")