import { useState } from "react";

const Form = (props) => {
  const [inputs, setInputs] = useState();

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(inputs);
    setInputs({});
    /// send inputs to backend
  };

  const handleInputs = (e) => {
    // const { value, checked, type, name } = e.target;
    // console.log(value, checked, type, name);
    const value =
      e.target.type === "checkbox" ? e.target.checked : e.target.value;
    setInputs({ ...inputs, [e.target.name]: value });
  };

  return (
    <>
      <h2>Contact</h2>
      <form onSubmit={handleSubmit}>
        <input
          onChange={(e) => handleInputs(e)}
          placeholder='Name...'
          name='name'
        />
        <br />
        <input
          onChange={(e) => handleInputs(e)}
          type='email'
          placeholder='Email...'
          name='email'
        />
        <br />
        <select name='num' onChange={(e) => handleInputs(e)}>
          <option value={-1}>Please select a number</option>
          <option value={1}>One</option>
          <option value={2}>Two</option>
          <option value={3}>Three</option>
        </select>
        <br />
        Yes/No{" "}
        <input
          checked={inputs?.yesno}
          name='yesno'
          onChange={(e) => handleInputs(e)}
          type='checkbox'
        />
        Diet{" "}
        <input name='diet' onChange={(e) => handleInputs(e)} type='checkbox' />
        Gloten Free{" "}
        <input name='free' onChange={(e) => handleInputs(e)} type='checkbox' />
        <br />
        male
        <input
          type='radio'
          value={"male"}
          name='radio'
          onChange={(e) => handleInputs(e)}
        />
        female{" "}
        <input
          type='radio'
          value={"female"}
          name='radio'
          onChange={(e) => handleInputs(e)}
        />
        <br />
        <textarea name='text' onChange={(e) => handleInputs(e)}></textarea>
        <br />
        <input type='submit' value='Submit' />
      </form>
    </>
  );
};
export default Form;

// const Form = (props) => {
//     const [name, setName] = useState("");
//     const [email, setEmail] = useState("");
//     const [num, setNum] = useState();
//     const [yesno, setYesNo] = useState(false);

//     const handleSubmit = (e) => {
//       e.preventDefault();
//       console.log(name, email, num, yesno);
//       // send to server
//       setName("");
//       setEmail("");
//     };

//     return (
//       <>
//         <h2>From</h2>
//         <form onSubmit={handleSubmit}>
//           <input
//             onChange={(e) => setName(e.target.value)}
//             placeholder='Name...'
//             value={name}
//           />
//           <br />
//           <input
//             onChange={(e) => setEmail(e.target.value)}
//             type='email'
//             placeholder='Email...'
//             value={email}
//           />
//           <br />
//           <select onChange={(e) => setNum(e.target.value)}>
//             <option value={1}>One</option>
//             <option value={2}>Two</option>
//             <option value={3}>Three</option>
//           </select>
//           <br />
//           Yes/No{" "}
//           <input
//             checked={yesno}
//             onChange={(e) => setYesNo(e.target.checked)}
//             type='checkbox'
//           />
//           <br />
//           <input type='submit' value='Submit' />
//         </form>
//       </>
//     );
//   };
//   export default Form;
