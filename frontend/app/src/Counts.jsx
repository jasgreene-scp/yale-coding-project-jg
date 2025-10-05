function Counts({ disease }) {
  if (!disease) return <p>Please select a disease to view counts.</p>;

  return (
    <div>
      <h2>Counts</h2>
      <p>Disease cohort count: [placeholder]</p>
      <p>Non-disease cohort count: [placeholder]</p>
    </div>
  );
}
export default Counts;
