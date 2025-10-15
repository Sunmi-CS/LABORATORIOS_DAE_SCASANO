import type { Movie } from '../../../shared/types/movie.types';
import MovieCard from '../components/MovieCard';

export interface MovieGridProps {
  movies: Movie[];
}

const MovieGrid = ({ movies }: MovieGridProps) => {
  return (
    <section id="now-showing" className="section">
      <div className="container d-flex f-direction-column g-8">
        <div className="d-flex f-direction-column a-items-center g-2">
          <h2 className="title c-primary t-align-center">
            Now Showing 🎬
          </h2>
          <p className="text text--lg c-secondary-text t-align-center">
            Discover the latest movies without spoilers - see everything you need to know!
          </p>
        </div>

        <div className="g-layout g-layout--auto-fit-columns g-8">
          {movies.length > 0 ? (
            movies.map(movie => <MovieCard key={movie.id} movie={movie} />)
          ) : (
            <div className="d-flex f-direction-column a-items-center g-4">
              <p className="text c-secondary-text">
                🎭 No movies available right now
              </p>
              <p className="text c-secondary-text">
                Check back soon for the latest releases!
              </p>
            </div>
          )}
        </div>
      </div>
    </section>
  );
};

export default MovieGrid;