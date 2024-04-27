import Header from "./component/Header/header";
import CanvasDrawing from "./component/Canvas/canvas";
import Result from "./component/Result/Result";
import "./App.css";

const App = () => {
  return (
    <>
      <Header />
      <div className="main">
        <div className="score">
          <Result />
        </div>
        <div className="canvas">
          <CanvasDrawing />
        </div>
      </div>
    </>
  );
};

export default App;
