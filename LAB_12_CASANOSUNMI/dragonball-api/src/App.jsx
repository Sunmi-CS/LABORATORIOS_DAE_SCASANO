//PRIMER CODE COLOCADO:


//import axios from 'axios';

//function App() {
  // --- Fetch API ---
  //const fetchData = async () => {
    //const response = await fetch('https://dragonball-api.com/api/characters');
    //const data = await response.json();
    //console.log('fetch:', data);
  //};

  // --- Axios ---
  //const axiosData = async () => {
    //const { data } = await axios.get('https://dragonball-api.com/api/characters');
    //console.log('axios:', data);
  //};

  // Llamamos ambas funciones una vez
  //fetchData();
  //axiosData();


// ------------------------------------------------------------------------------
// SEGUNDO CODE:

//import axios from 'axios';
//import { useEffect, useState } from 'react';
//
//const getAllCharacters = async () => {
 // const { data } = await axios.get('https://dragonball-api.com/api/characters');
  //return data;
//};

//function App() {
  //const [response, setResponse] = useState({});

  //useEffect(() => {
   // const fetchData = async () => {
   //   const dataFetched = await getAllCharacters();
   //   setResponse(dataFetched);
    //};

    //fetchData();
  //}, []);

//  console.log(response);

// ------------------------------------------------------------------------------
// TERCER CODE:








import axios from 'axios';
import { useEffect, useState } from 'react';

const getAllCharacters = async () => {
  const { data } = await axios.get('https://dragonball-api.com/api/characters');
  return data;
};

function App() {
  const [response, setResponse] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      const dataFetched = await getAllCharacters();
      setResponse(dataFetched);
      setLoading(false);
    };

    fetchData();
  }, []);

  console.log(response);

  return (
    <section className="py-4">
      <div className="container">
        <h2 className="text-center">Dragonball API</h2>
        <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
          {loading ? (
            <div className="text-center">
              <div className="spinner-grow text-primary" role="status">
                <span className="visually-hidden">Loading...</span>
              </div>
            </div>
          ) : (
            response.items?.map((character) => {
              const { id, name, description, image } = character;
              return (
                <div key={id} className="col">
                  <div className="card shadow-sm">
                    <img
                      src={image}
                      alt={name}
                      style={{ height: '256px', objectFit: 'contain' }}
                    />
                    <div className="card-body">
                      <h5 className="card-title">{name}</h5>
                      <p className="card-text">
                        {description.slice(0, 100)}...
                      </p>
                      <div className="d-flex justify-content-between align-items-center">
                        <div className="btn-group">
                          <button
                            type="button"
                            className="btn btn-sm btn-outline-secondary"
                          >
                            View
                          </button>
                          <button
                            type="button"
                            className="btn btn-sm btn-outline-secondary"
                          >
                            Edit
                          </button>
                        </div>
                        <small className="text-body-secondary">9 mins</small>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })
          )}
        </div>
      </div>
    </section>
  );
}

export default App;
