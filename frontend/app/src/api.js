const BASE_URL = "http://localhost:8000/";

export const api = {
  auth: async (payload) => {
    const res = await fetch(`${BASE_URL}/auth`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    return res.json();
  },

  counts: async (disease) => {
    const res = await fetch(`${BASE_URL}/counts?disease=${disease}`);
    return res.json();
  },

  agePlot: async (disease) => {
    const res = await fetch(`${BASE_URL}/age_distribution?disease=${disease}`);
    return res.json();
  },

  sexPlot: async (disease) => {
    const res = await fetch(`${BASE_URL}/sex_distribution?disease=${disease}`);
    return res.json();
  },

  boxPlot: async (disease, measurement) => {
    const res = await fetch(
      `${BASE_URL}/box-plot?disease=${disease}&measurement=${measurement}`
    );
    return res.json();
  },

  summaryStats: async (disease) => {
    const res = await fetch(`${BASE_URL}/stats?disease=${disease}`);
    return res.json();
  },
};
