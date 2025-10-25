import Greeting from "./components/Greeting";
import Title from "./components/Title";
import InstituteCard from "./components/InstituteCard";

function App() {

  const institutes = [
    {
      title: "TECSUP",
      text: "Instituto líder en tecnología e innovación educativa.",
      image:"https://app.tecsup.edu.pe/matricula/web/graficos/ingreso_tecsup.png",
      link: "https://www.tecsup.edu.pe",
    },
    {
      title: "IDAT",
      text: "Educación moderna para el futuro profesional.",
      image:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8admQXkjpSUAu8uaFkdKZjC6ixYlEfZXRWA&s",
      link: "https://www.idat.edu.pe",
    },
    {
      title: "SENATI",
      text: "Formación técnica para la industria peruana.",
      image: "https://elpopular.cronosmedia.glr.pe/original/2022/05/23/628bd3ec96431b5a117b1c8d.jpg",
      link: "https://www.senati.edu.pe",
    },
    {
      title: "ISIL",
      text: "Educación enfocada en innovación y empleabilidad.",
      image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_dZKKI3mhNlQ0GX4PFacaWQZ2kjCaq4D4mw&s",
      link: "https://www.isil.pe",
    },
    {
      title: "CERTUS",
      text: "Instituto de educación superior con enfoque práctico.",
      image: "https://www.certus.edu.pe/wp-content/uploads/2019/01/sede-callao-min.jpg",
      link: "https://www.certus.edu.pe",
    },
    {
      title: "CIBERTEC",
      text: "Formación técnica y profesional en tecnología e innovación.",
      image: "https://www.cibertec.edu.pe/directus/e28058d6-4a4f-47ca-81aa-ffe306686aa3.jpg",
      link: "https://www.cibertec.edu.pe",
    },
    {
      title: "SISE",
      text: "Instituto enfocado en desarrollo profesional y tecnológico.",
      image: "https://www.sise.edu.pe/uploads/Villa_el_salvador_7dcec54a08.jpg",
      link: "https://www.sise.edu.pe",
    },
    {
      title: "ZEGEL IPAE",
      text: "Educación empresarial e innovación para el éxito profesional.",
      image: "https://elcomercio.pe/resizer/r3zYYsUANakejed5NW8J-Z1JyGw=/1200x1200/smart/filters:format(jpeg):quality(75)/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/65WJTHSZGJDO3H2R6VJWEF5IXU.jpg",
      link: "https://www.zegelipae.edu.pe",
    },
    {
      title: "TOULOUSE LAUTREC",
      text: "Educación creativa e innovadora para el futuro profesional.",
      image: "https://www.toulouselautrec.edu.pe/sites/default/files/styles/438x302/public/campus/toulouse%20lautrec%20sede%20chacarilla.jpg?itok=qTxKyt7K",
      link: "https://www.toulouselautrec.edu.pe",
    },
  ];

  return (
    <div className="container text-center mt-4">
      <Title />
      <Greeting name="Estudiante" />

      <div className="d-flex flex-wrap justify-content-center gap-4 mt-4">
        {institutes.map((inst, index) => (
          <InstituteCard
            key={index}
            title={inst.title}
            text={inst.text}
            image={inst.image}
            link={inst.link}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
