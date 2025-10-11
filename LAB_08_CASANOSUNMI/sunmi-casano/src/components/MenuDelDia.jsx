import React from 'react';
import lomo from '../assets/lomo.png';
import ceviche from '../assets/ceviche.JPEG'
import trucha from '../assets/trucha.jpg'
import aji from '../assets/aji.jpeg'



function MenuDelDia() {
  return (
    <div>
      <h2>Menú del Día</h2>
      <p> Pollo al horno con papas</p>
      <img src={lomo} alt="Pollo al horno con papas" width="300" />

      <p> Ceviche</p>
      <img src={ceviche} alt="Pollo al horno con papas" width="300" />


      <p> Trucha Frita</p>
      <img src={trucha} alt="Pollo al horno con papas" width="300" />


      <p> Pollo al horno con papas</p>
      <img src={aji} alt="Pollo al horno con papas" width="300" />
        

    </div>
  );
}

export default MenuDelDia;
