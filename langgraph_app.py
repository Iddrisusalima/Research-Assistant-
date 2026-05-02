import argparse

def main():
    parser = argparse.ArgumentParser(description='Simple Research Assistant placeholder')
    parser.add_argument('--query', '-q', type=str, default='', help='Research question to answer')
    args = parser.parse_args()

    if not args.query:
        print('Hello from langgraph_app.py!')
        print('Usage: python langgraph_app.py -q "your question"')
        return

    question = args.query.strip()
    print(f'Received query: {question}')
    print('This is a placeholder response. Replace this section with your LLM/RAG implementation.')


if __name__ == "__main__":
    main()
