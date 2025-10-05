function AgePlot({ disease }) {
  if (!disease) return <p>Please select a disease to view age distribution.</p>;
  return (
    <div>
      <h3>Age Distribution</h3>
      <p>[Plot placeholder]</p>
    </div>
  );
}
export default AgePlot;
