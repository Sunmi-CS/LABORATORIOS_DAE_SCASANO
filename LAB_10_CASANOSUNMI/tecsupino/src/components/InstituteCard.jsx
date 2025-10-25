function InstituteCard({ title, text, image, link }) {
  return (
    <div className="card shadow-sm" style={{ width: "18rem" }}>
      <img src={image} className="card-img-top" alt={title} />
      <div className="card-body">
        <h5 className="card-title">{title}</h5>
        <p className="card-text">{text}</p>
        <a href={link} className="btn btn-primary">
          Ver más
        </a>
      </div>
    </div>
  );
}

export default InstituteCard;
