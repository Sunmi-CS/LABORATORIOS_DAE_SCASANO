import type { Movie } from "./shared/types/movie.types";
import Footer from "./ui/components/layouts/Footer";
import Header from "./ui/components/layouts/Header";
import Hero from "./ui/components/modules/Hero";
import MovieGrid from "./ui/components/modules/MovieGrid";
import { getMoviesFromMockData } from "./utils/movie.utils";

const App = () => {
  const movies: Movie[] = getMoviesFromMockData();

  return (
    <>
      <Header />
      <main className="main">
        <Hero />
        <MovieGrid movies={movies} />
      </main>
      <Footer />
    </>
  );
};

export default App;