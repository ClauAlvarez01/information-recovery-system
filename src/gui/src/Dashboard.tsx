import SearchBar from "./SearchBar";

function Dashboard() {
    return (
        <>
            <div className="min-h-full">

                <div className="shadow-xl">
                    <nav className="bg-sky-300 shadow-lg">
                        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 sha">
                            <div className="flex h-16 items-center justify-between">
                                <div className="flex items-center">
                                    <div className="flex-shrink-0">
                                        <img className="h-10 mt-1" src="logo.png" alt="Your Company" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </nav>
                </div>

                <main>
                    <div className="mx-auto mt-10 max-w-7xl py-6 sm:px-6 lg:px-8">
                        <SearchBar/>
                    </div>
                </main>
            </div>
        </>
    );
}

export default Dashboard;
