import { createContext, useState } from "react";
import Title from "./Title";
export const DisplayContext = createContext();

import ShowCounter from "./ShowCounter";
const Display = (props) => {
  const [title,setTitle] = useState('my titlecvbvbcvb')
  return (
    <>
      <h2>Display</h2>
      <DisplayContext.Provider value={{ title,setTitle }}>
        <ShowCounter />
        
      </DisplayContext.Provider>
    </>
  );
};
export default Display;
