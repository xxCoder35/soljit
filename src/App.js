import logo from './logo.svg';
import './App.css';
import CandidTable from './components/CandidTable' ;
import Form from './components/form'

function App() {
  return (
    <div className="App">
      <h1> Candidats salesforce</h1>
       <CandidTable></CandidTable>
       <Form/>
    </div>
  );
}

export default App;
