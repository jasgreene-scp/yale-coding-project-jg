import React, { useState } from "react";
import Header from "./Header";
import Auth from "./Auth";
import DiseaseSelector from "./DiseaseSelector";
import MeasurementSelector from "./MeasurementSelector";
import Counts from "./Counts";
import AgePlot from "./AgePlot";
import SexPlot from "./SexPlot";
import BoxPlot from "./BoxPlot";
import SummaryStatsTable from "./SummaryStatsTable";

function App() {
  const [selectedDisease, setSelectedDisease] = useState("");
  const [selectedMeasurement, setSelectedMeasurement] = useState("");

  return (
    <div>
      <Auth />
      <DiseaseSelector onSelect={setSelectedDisease} />
      <MeasurementSelector onSelect={setSelectedMeasurement} />
      <Counts disease={selectedDisease} />
      <AgePlot disease={selectedDisease} />
      <SexPlot disease={selectedDisease} />
      <BoxPlot disease={selectedDisease} measurement={selectedMeasurement} />
      <SummaryStatsTable disease={selectedDisease} />
    </div>
  );
}

export default App;
