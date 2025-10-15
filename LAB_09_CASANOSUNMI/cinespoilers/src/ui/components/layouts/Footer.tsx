const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <nav className="nav">
        <div className="container g-layout g-layout--auto-fit-columns g-10">
          <div className="d-flex f-direction-column g-2">
            <a href="#">
              <img
                src="/logo.svg"
                alt="Cine SpoilerS Logo"
                width="32"
                height="32"
                className="img img--logo"
              />
            </a>
            <h2 className="interactive interactive--lg c-primary">
              Cine SpoilerS
            </h2>
            <p className="text text--xs c-secondary-text">
              AI-powered cinema experience. See everything about movies without spoilers! 🎬✨
            </p>
          </div>

          <div className="d-flex f-direction-column g-2">
            <h3 className="interactive interactive--lg">Showtimes</h3>
            <ul className="list d-flex f-direction-column g-1">
              <li>
                <a href="#now-showing" className="link interactive interactive--sm c-secondary-text">
                  🎞️ Now Showing
                </a>
              </li>
              <li>
                <a href="#coming-soon" className="link interactive interactive--sm c-secondary-text">
                  🔜 Coming Soon
                </a>
              </li>
              <li>
                <a href="#premieres" className="link interactive interactive--sm c-secondary-text">
                  🌟 Premiere Events
                </a>
              </li>
            </ul>
          </div>

          <div className="d-flex f-direction-column g-2">
            <h3 className="interactive interactive--lg">Explore</h3>
            <ul className="list d-flex f-direction-column g-1">
              <li>
                <a href="#faq" className="link interactive interactive--sm c-secondary-text">
                  ❓ FAQs
                </a>
              </li>
              <li>
                <a href="#about" className="link interactive interactive--sm c-secondary-text">
                  📖 About Us
                </a>
              </li>
              <li>
                <a href="#blog" className="link interactive interactive--sm c-secondary-text">
                  📝 Cinema Blog
                </a>
              </li>
            </ul>
          </div>

          <div className="d-flex f-direction-column g-2">
            <h3 className="interactive interactive--lg">Connect</h3>
            <ul className="list d-flex f-direction-column g-1">
              <li>
                <a
                  href="https://www.instagram.com/elliotgaramendi/"
                  className="link interactive interactive--sm c-secondary-text"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  📸 Instagram
                </a>
              </li>
              <li>
                <a
                  href="https://x.com/elliotgaramendi"
                  className="link interactive interactive--sm c-secondary-text"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  🐦 Twitter/X
                </a>
              </li>
              <li>
                <a
                  href="https://www.youtube.com/@elliotgaramendi"
                  className="link interactive interactive--sm c-secondary-text"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  🎥 YouTube
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <nav className="nav">
        <div className="container flexbox flexbox--centered-spacing flexbox--responsive g-2">
          <h2 className="interactive interactive--xs">
            <a
              href="https://www.linkedin.com/in/elliotgaramendi/"
              className="link interactive interactive--xs"
              target="_blank"
              rel="noopener noreferrer"
            >
              Elliot Garamendi
            </a>
            &copy; {currentYear} Cine SpoilerS. All rights reserved.
          </h2>
          <h2 className="interactive interactive--xs">
            Made with ❤️ by: <a href="https://www.instagram.com/elliotgaramendi/" className="link interactive interactive--xs">
              Elliot Garamendi
            </a> for movie lovers! 🍿
          </h2>
        </div>
      </nav>
    </footer>
  );
};

export default Footer;