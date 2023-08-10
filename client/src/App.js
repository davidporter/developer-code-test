import React, { useState, useEffect } from 'react' // useState creates a state variable that uses the data retrieved from the backend

function App() {

  const [data, setData] = useState([{}])
  const [artwork_data, artwork_setData] = useState([{}])


  useEffect(() => {
    fetch("/artwork").then(
      res => res.json()
    ).then(
      artwork_data => {
        artwork_setData(artwork_data)
      }
    )
  }, [])

  
  useEffect(() => {
    fetch("/exhibition").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
      }
    )
  }, [])


  return (

    <div>
      <h2>David Porter developer-code-test-v2</h2>
      
      <h3>Exhibition: "Sacred Gifts and Worldly Treasures: Medieval Masterworks from the Cleveland Museum of Art"</h3>
      <h4>Returns all "Christian" works from the exhibition, as identified in the "culture" field.</h4>
          <li><font color="blue">Use CMA’s Open Access API to extract a “highlight” artwork based on criteria you decide (e.g. biggest, smallest, oldest, longest artist first name, etc.) from a CMA exhibition of your choosing (current or past) that has at least 8 CMA-owned works (CMA exhibitions often have many works on loan. The API response will only show CMA-owned works. You may have to look at a few exhibitions to find one with more than 8 works!).</font></li>

      {(typeof data.exhibition === 'undefined') ? (
        <p>loading, takes 10 seconds...</p>        
      ) : (   
        data.exhibition.map((art, i) => (
          <p key={i}>{art}</p>        
        ))
      )}   

      <hr/>


      <h3>Monet "mini" Exhibition:</h3>
      <h4>Returns 5 artworks with "Monet" as the keyword</h4>
      <li><font color="blue">
      Use the API to find 5 artworks (in or out of the exhibition you chose) that are related by one or more criteria in the artwork data to create a “mini exhibition”.</font>
      </li>
      {(typeof artwork_data.artworks === 'undefined') ? (
        <p>loading...</p>
      ) : (
        artwork_data.artworks.map((art, i) => (
        <p>{art}</p>
        ))
      )}    
      <hr/>
      

    </div>
  )
}

export default App