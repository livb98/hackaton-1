import { useContext } from "react";
import { AppContext } from "../App";
import { DisplayContext } from "./Display";
import Title from "./Title";

const ShowCounter = (props) => {
  const { count, name } = useContext(AppContext);
  const {title}  = useContext(DisplayContext);
  return (
    <>
     <h1>{title}</h1>
      <h3>ShowCounter {name}</h3>
      {count}
      <Title/>
    </>
  );
};
export default ShowCounter;
