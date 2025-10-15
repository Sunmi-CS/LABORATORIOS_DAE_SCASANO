import { tmdbGenresMock, tmdbNowPlayingMock } from "../shared/mocks/tmdb.mock";
import type { Movie } from "../shared/types/movie.types";
import type { TMDBMovie } from "../shared/types/tmdb.types";

export const getImageUrl = (size = 'w342', path: string | null): string => {
  if (!path) return `https://picsum.photos/342/513?random=${Math.floor(Math.random() * 1000)}`;
  return `https://image.tmdb.org/t/p/${size}${path}`;
};

const generateRandomDuration = (): string => {
  const durations = [
    '85 min', '90 min', '95 min', '100 min', '105 min', '110 min', '115 min', '120 min',
    '125 min', '130 min', '135 min', '140 min', '145 min', '150 min', '155 min', '160 min'
  ];
  return durations[Math.floor(Math.random() * durations.length)];
};

const createGenreMap = () => {
  const genreMap: Record<number, { id: number; name: string }> = {};
  tmdbGenresMock.genres.forEach(genre => {
    genreMap[genre.id] = { id: genre.id, name: genre.name };
  });
  return genreMap;
};

const genreMap = createGenreMap();

const getMovieGenres = (genreIds: number[]) => {
  return genreIds
    .map(id => genreMap[id])
    .filter(Boolean);
};

const generateRandomShowTimes = (): string[] => {
  const allTimes = ['1:00 PM', '2:30 PM', '4:00 PM', '5:45 PM', '7:15 PM', '9:00 PM', '10:30 PM', '11:30 PM'];
  const shuffled = allTimes.sort(() => Math.random() - 0.5);
  const numTimes = Math.floor(Math.random() * 4) + 3;
  return shuffled.slice(0, numTimes);
};

export const adaptTmdbToMovie = (tmdbMovie: TMDBMovie): Movie => {
  return {
    id: tmdbMovie.id,
    title: tmdbMovie.title,
    description: tmdbMovie.overview,
    duration: generateRandomDuration(),
    releaseDate: tmdbMovie.release_date,
    poster: getImageUrl('w342', tmdbMovie.poster_path),
    genres: getMovieGenres(tmdbMovie.genre_ids),
    showTimes: generateRandomShowTimes(),
    rating: Math.round(tmdbMovie.vote_average) / 2,
  };
};

export const adaptTmdbMovies = (tmdbMovies: TMDBMovie[]): Movie[] => {
  return tmdbMovies.map(adaptTmdbToMovie);
};

export const getMoviesFromMockData = (): Movie[] => {
  return adaptTmdbMovies(tmdbNowPlayingMock.results);
};