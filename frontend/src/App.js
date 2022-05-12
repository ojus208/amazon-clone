import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';


/// imports all components
import Nav from './components/nav'
import Body from './components/body'
import Deal_page  from './components/deal_page';

function App() {
  return (
    <Router>
      <div className="App">
        <Nav />
        <Switch>
          <Route path='/' exact  >
          <Body />
          </Route>
          <Route path={`/Deals/:deal_id`}  >
          <Deal_page />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
