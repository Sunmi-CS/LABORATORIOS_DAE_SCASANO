const Hero = () => {
  return (
    <article className="hero">
      <div className="container d-flex f-direction-column a-items-center g-4">
        <h1 className="hero__title t-align-center">
          🎥 Explore spoiler-free cinema with <span className="c-primary">AI-Powered insights ✨</span>
        </h1>
        <p className="hero__paragraph t-align-center">
          👋 Welcome to <span className="f-weight-700">Cine SpoilerS</span> 🍿 where you can see everything about movies without the spoilers 🚫. Discover premieres 🌟, reviews 📝, and interactive AR experiences 🔍
        </p>
        <div className="d-flex g-4">
          <a
            href="#now-showing"
            className="button button--primary interactive interactive--xl"
          >
            🎬 Now Showing
          </a>
          <a
            href="#coming-soon"
            className="button button--outline-primary interactive interactive--xl"
          >
            🔮 Coming Soon
          </a>
        </div>
      </div>
    </article>
  );
};

export default Hero;