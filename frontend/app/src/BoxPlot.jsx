function BoxPlot({ disease, measurement }) {
  if (!disease || !measurement)
    return (
      <p>
        Please select a disease, and its corresponding measuremnt to view age
        distribution.
      </p>
    );

  return (
    <div>
      <h2>Box Plot</h2>
      <p>[Interactive plot placeholder]</p>
    </div>
  );
}
export default BoxPlot;
