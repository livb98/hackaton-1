import { useContext } from "react";
import { AppContext } from "../App";

const ButtonTwo = (props) => {
  const { count, setCount } = useContext(AppContext);
  return (
    <>
      <button onClick={() => setCount(count + 1)}> button 2 +</button>
    </>
  );
};
export default ButtonTwo;
