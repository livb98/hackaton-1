import { useState, createContext } from "react";
import "./App.css";
import Display from "./components/Display";
import Action from "./components/Action";
/**
         APP
        /    \
  Display    Action    
    /           \
ShowCounter     Button   
                  \
                  ButtonTwo

 */

export const AppContext = createContext();

function App() {
  const [count, setCount] = useState(555);
  const fetchData = () => {

  }
  return (
    <>
      <div>
        <h2>useContext / createContext</h2>
        <h2>Counter</h2>
        <AppContext.Provider value={{ count, setCount, name:'zivuch', fetchData }}>
          <Display />
          <Action />
        </AppContext.Provider>
      </div>
    </>
  );
}

export default App;
