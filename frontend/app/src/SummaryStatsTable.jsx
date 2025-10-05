function SummaryStatsTable({ disease }) {
  if (!disease)
    return <p>Please select a disease to view Summary Stats Table.</p>;

  return (
    <div>
      <h2>Summary Stats</h2>
      <p>[Table placeholder for disease and non-disease]</p>
    </div>
  );
}
export default SummaryStatsTable;
