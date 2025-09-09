import { useState , useEffect} from 'react';
import axios from "axios";
import './App.css'

function App() {
  const [cars, setCars] = useState([])
  const [name, setName] = useState("")
  const [colour, setColour] = useState("black")

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/cars/")
    .then(res => setCars(res.data))
    .catch(err => console.error(err));

  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://127.0.0.1:8000/api/cars/", { name, colour})
    .then(res => {
        setCars([...cars, res.data]);
        setName("");
        setColour("black");
      })
      .catch(err => console.error(err));
  };
  

  return (
    <div className="main-wrapper">
      <h1>Car Collection</h1>

      <form onSubmit={handleSubmit}>
        <input 
        type="text"
        placeholder='Car Name'
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
        />

        <select value={colour} onChange={(e) => setColour(e.target.value)}>
          <option value="red">Red</option>
          <option value="blue">Blue</option>
          <option value="green">Green</option>
          <option value="black">Black</option>
        </select>

        <button type="submit">Add Car</button>

      </form>

      <h2>My Cars</h2>
      <ul>
        {cars.map((car) => (
          <li key={car.id}>
            <h3>{car.name}</h3>
            {car.name} - {car.colour} 
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
