export interface Movie {
  id: number;
  title: string;
  description: string;
  duration: string;
  releaseDate: string;
  poster: string;
  genres: Genre[];
  showTimes: string[];
  rating: number;
}

export interface Genre {
  id: number;
  name: string;
}