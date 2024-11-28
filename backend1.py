from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': '192.168.0.59', 'port': 9200, 'scheme': 'http'}])

INDEX_NAME = 'events3'

@app.route('/filter', methods=['POST'])
def filter_events():
    filters = request.json
    query = {
        "query": {
            "bool": {
                "must": [],
                "filter": []
            }
        }
    }

    # Add City filter if provided
    if 'city' in filters and filters['city']:
        query['query']['bool']['must'].append({
            "match": {"City": filters['city']}
        })

    # Add Genre filter if provided
    if 'genre' in filters and filters['genre']:
        query['query']['bool']['must'].append({
            "match": {"Genre": filters['genre']}
        })

    # Add PriceRange filter if provided
    if 'price_min' in filters and 'price_max' in filters:
        query['query']['bool']['filter'].append({
            "range": {
                "PriceRange": {
                    "gte": filters['price_min'],
                    "lte": filters['price_max']
                }
            }
        })

    # Get size parameter from filters, default to 1000
    size = filters.get('size', 1000)  # Fetch up to 1000 rows by default

    # Execute the query
    try:
        response = es.search(index=INDEX_NAME, body=query, size=size)
        hits = response['hits']['hits']
        results = [hit['_source'] for hit in hits]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
