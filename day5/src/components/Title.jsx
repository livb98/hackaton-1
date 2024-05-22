import { useContext } from "react";
import { DisplayContext } from "./Display";
const Title = (props) => {
  const { setTitle } = useContext(DisplayContext);
  return (
    <>
      <input
        onChange={(e) => setTitle(e.target.value)}
        placeholder='title...'
      />
    </>
  );
};
export default Title;
