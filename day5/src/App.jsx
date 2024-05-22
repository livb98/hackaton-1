// import { useState, useRef, useEffect, useReducer } from "react";
// import "./App.css";
// import Counter from "./reducer";

// function App() {
//   // const [title, setTitle] = useState("my title");
//   // let name = "Dan";
//   // const nameRef = useRef("Dan Ref");

//   // useEffect(()=>{
//   //    name = 'aaa';
//   //    nameRef.current = 'bbb'
//   //    setTitle('ccc')
//   // },[])

//   // const changeName = () => {
//   //   name = "John";
//   //   nameRef.current = "John Ref";
//   //   console.log(name);
//   //   console.log(nameRef.current);
//   // };
//   // const changeTitle = () => {
//   //   setTitle("Title Title");
//   // };
//   reducer()
//   return (
//     <>
//       {/* <div>
//         <h1>{name}</h1>
//         <button onClick={changeName}>Change Name</button>
//       </div>
//       <div>
//         <h1>{nameRef.current}</h1>
//         <button onClick={changeName}>Change Name Ref</button>
//       </div>
//       <div>
//         <h1>{title}</h1>
//         <button onClick={changeTitle}>Change Title</button> */}
//       {/* </div> */}
//       <Counter/>
//     </>
//   );
// }

// export default App;

import { useState, useRef, useEffect, useReducer } from "react";
import "./App.css";
import Counter from "./reducer";
import { TodoList } from "./reducer";
// Define your reducer function
const reducer = (state, action) => {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
};

function App() {
  // Initialize state using useReducer
  // const [state, dispatch] = useReducer(reducer, { count: 0 });
  const [todos,dispatch] = useReducer(reducer,[])

  return (
    <>
      {/* Render Counter component and pass state and dispatch function */}
      {/* <Counter state={state} dispatch={dispatch} /> */}
      <TodoList state={todos} dispatch={dispatch}/>
    </>
  );
}

export default App;

