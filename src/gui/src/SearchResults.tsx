import { Document } from "./types/types";

interface Props {
  results: Document[];
}

function SearchResults({ results }: Props) {
  function truncateString(text: string): string {
    const maxLength = 300;
    if (text.length <= maxLength) {
      return text;
    } else {
      const truncatedText = text.slice(0, maxLength);
      return `${truncatedText}...`;
    }
  }

  return (
    <>
      {results.length > 0 && (
        <div className="flex flex-row mb-20">
          <div className="lg:ml-20 text-left w-full">
            {results.map((doc) => (
              <div className="mb-4 p-4">
                <h2 className="text-xl font-semibold font-serif">
                  {doc.title}
                </h2>
                <h3 className="text-md font-light mb-2">{doc.author}</h3>
                <p className="text-gray-600 mb-2 max-w-2xl">
                  {truncateString(doc.text)}
                </p>
              </div>
            ))}
          </div>
          <div className="bg-gray-300 w-auto min-w-64 lg:mr-20">Metrics</div>
        </div>
      )}
    </>
  );
}

export default SearchResults;
