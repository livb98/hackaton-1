import Form from "./components/Form";
import Home from "./components/Home";
import About from "./components/About";
import Nav from "./components/Nav";
import Shop from "./components/Shop";
import Product from "./components/Product";
import "./App.css";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <Nav />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about' element={<About />} />
        <Route
          path='/contact'
          element={
            <>
              <Form />
            </>
          }
        />
        <Route path='/shop' element={<Shop />} />
        <Route path='/product/:id' element={<Product />} />
        <Route
          path='*'
          element={
            <>
              <h2>404 not found</h2>
            </>
          }
        />
      </Routes>
    </>
  );
}

export default App;
