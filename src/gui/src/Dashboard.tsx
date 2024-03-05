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
  const [query, setQuery] = useState("")

  const toggle = () => setShowQueries(!showQueries)

  function handleSearch(newQuery=query){
    // Make request
    console.log("Trim = " + newQuery.trim());

    const request = { 'query': newQuery }

    if (newQuery.trim() !== '') {
      axios.get('http://localhost:8000/api/search/', {
        params: request
      })
        .then(response => {
          setSearchResults(response.data.docs);
          setMetrics(response.data.metrics);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }

  useEffect(() => {
    const fetchData = async () => {
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
              <div className="flex h-16 items-center justify-start">
                <div className="flex items-center w-full">
                  <div className="flex-shrink-0">
                    <img
                      className="h-12 mt-5"
                      src="logo.png"
                      alt="Searchify"
                    />
                  </div>
                    <div className="ml-10 abs mr-auto mt-5 space-x-4 w-full">
                      <div className=" float-end">
                        <a className="bg-gray-700 hover:bg-gray-800 hover:cursor-pointer text-white rounded-lg px-3 py-2 ml-auto text-sm font-medium" onClick={toggle}>Queries</a>
                      </div>
                      <Queries open={showQueries} setOpen={setShowQueries} queries={queries} searchFunction={handleSearch}/>
                    </div>
                </div>
              </div>
            </div>
          </nav>
        </div>

        <main>
          <div className="mx-auto mt-10 max-w-7xl py-6 sm:px-6 lg:px-8">
            <SearchBar setQuery={setQuery} searchFunction={handleSearch}/>
          </div>

          <SearchResults results={searchResults} metrics={metrics} />
        
        </main>
      </div>
    </>
  );
}

export default Dashboard;
