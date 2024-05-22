import { Link } from "react-router-dom";
const Nav = (props) => {
  return (
    <header>
      <nav>
        <Link style={{ color: "red" }} to='/'>
          Home
        </Link>{" "}
        <Link to='/about#section1'>About</Link>{" "}
        <Link to='/contact'>Contact</Link>{" "}
        <Link to='/shop'>Shop</Link>
      </nav>
    </header>
  );
};
export default Nav;
