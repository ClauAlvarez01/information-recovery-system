import { Document, Metrics } from "./types/types";
import { ChartBarSquareIcon } from "@heroicons/react/24/outline";
interface Props {
  results: Document[];
  metrics: Metrics|undefined;
}

function SearchResults({ results, metrics }: Props) {
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
            {results.map((doc, index) => (
              <div className="mb-4 p-4" key={index}>
                <div className="flex">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      className="w-6 h-6 mr-2"
                    >
                      <path
                        d="M12 7.5h1.5m-1.5 3h1.5m-7.5 3h7.5m-7.5 3h7.5m3-9h3.375c.621 0 1.125.504 1.125 1.125V18a2.25 2.25 0 0 1-2.25 2.25M16.5 7.5V18a2.25 2.25 0 0 0 2.25 2.25M16.5 7.5V4.875c0-.621-.504-1.125-1.125-1.125H4.125C3.504 3.75 3 4.254 3 4.875V18a2.25 2.25 0 0 0 2.25 2.25h13.5M6 7.5h3v3H6v-3Z"
                      />
                    </svg>
                    <h2 className="text-xl font-semibold font-serif">
                      {doc.title}
                    </h2>
                </div>

                <h3 className="text-md font-light mb-2">{doc.author}</h3>
                <p className="text-gray-600 mb-2 max-w-2xl">
                  {truncateString(doc.text)}
                </p>
              </div>
            ))}
          </div>
          {metrics && <div className="w-auto min-w-64 lg:mr-20 p-5 border h-full bg-gray-50 text-left rounded-xl">
            
            <div className="flex items-center">
              <div>
                <ChartBarSquareIcon className="h-8 center"/>
              </div>
              <label className="text-3xl">Metrics:</label>
            </div>

            <div className="mt-10">
                <label className="text-lg shadow-sm">Precision:</label>
                <p className="font-mono">Boolean: {metrics.precision.boolean}</p>
                <p className="font-mono">Other: {metrics.precision.other}</p>
            </div>
            
            <div className="mt-5">
                <label className="text-lg shadow-sm">Recovered:</label>
                <p className="font-mono">Boolean: {metrics.recovered.boolean}</p>
                <p className="font-mono">Other: {metrics.recovered.other}</p>
            </div>

            <div className="mt-5">
                <label className="text-lg shadow-sm">F1:</label>
                <p className="font-mono">Boolean: {metrics.f1.boolean}</p>
                <p className="font-mono">Other: {metrics.f1.other}</p>
            </div>

            <div className="mt-5">
                <label className="text-lg shadow-sm">Fallout:</label>
                <p className="font-mono">Boolean: {metrics.fallout.boolean}</p>
                <p className="font-mono">Other: {metrics.fallout.other}</p>
            </div>

          </div>}
        </div>
      )}
    </>
  );
}

export default SearchResults;
