// import Form from "./components/Form";
import Home from "./components/Home";
import About from "./components/About";
import Nav from "./components/Nav";
import Shop from "./components/Shop";
import Product from "./components/Product";
import "./App.css";
import {
  Link,
  createBrowserRouter,
  RouterProvider,
  Outlet,
} from "react-router-dom";


/** Rountering */
const Root = () => {
  return (
    <>
      <Nav/>
      <Outlet />
      <footer>
        copyright 2024 student of de
      </footer>
   </>
  );
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <h2>Opps...</h2>,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/about",
        element: <About />,
      },
      {
        path: "/shop",
        element: <Shop />,
      },
      {
        path: "/product/:id",
        element: <Product />,
      },
    ],
  },
]);

function App() {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
