import { useEffect, useState } from "react";
import SearchBar from "./SearchBar";
import axios from "axios";
import { Document, Metrics, Query } from "./types/types";
import SearchResults from "./SearchResults";
import Queries from "./Queries";

function Dashboard() {
  const [searchResults, setSearchResults] = useState<Document[]>([]);
  const [metrics, setMetrics] = useState<Metrics>();
  const [queries, setQueries] = useState<Query[]>();
  const [showQueries, setShowQueries] = useState(false)

  const toggle = () => setShowQueries(!showQueries)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/test/");
        setSearchResults(response.data.docs);
        setMetrics(response.data.metrics);
      } catch (error) {
        console.error("Error fetching data:", error);
      }

      try {
        const response = await axios.get("http://localhost:8000/api/queries/");
        setQueries(response.data.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <>
      <div className="min-h-full">
        <div className="shadow-xl">
          <nav className="bg-sky-300 h-20 shadow-lg">
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 sha">
              <div className="flex h-16 items-center justify-between">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <img
                      className="h-12 mt-5"
                      src="logo.png"
                      alt="Searchify"
                    />
                  </div>
                  <div className="mt-5">
                    <div className="ml-10 flex items-baseline space-x-4 justify-end">
                      <a className="bg-gray-700 hover:bg-gray-800 hover:cursor-pointer text-white rounded-lg px-3 py-2 text-sm font-medium" onClick={toggle}>Queries</a>
                      <Queries open={showQueries} setOpen={setShowQueries} queries={queries}/>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </nav>
        </div>

        <main>
          <div className="mx-auto mt-10 max-w-7xl py-6 sm:px-6 lg:px-8">
            <SearchBar />
          </div>

          <SearchResults results={searchResults} metrics={metrics} />
        
        </main>
      </div>
    </>
  );
}

export default Dashboard;
