(() => {
  const state = {
    ifId: "false",
    ifPw: "false",
  };
  u("input").on("change", (e) => {
    e.currentTarget.value = e.currentTarget.value.replace(/[^0-9a-zA-Z]/g, "");
    if (e.currentTarget.value.length > 20) {
      console.log("im in");
      e.currentTarget.value = e.currentTarget.value.slice(0, 20);
    }
  });

  u(".input-id").on("change", async (e) => {
    const res = await fetch(
      `http://localhost:8000/user/id?id=${e.currentTarget.value}`
    );
    const json = await res.json();
    if (json.result) {
      u("#error-id").nodes.at(0).style.display = "block";
      state.ifId = false;
    } else {
      u("#error-id").nodes.at(0).style.display = "none";
      state.ifId = true;
    }
    console.log(json);
  });
  u(document).on("submit", (e) => {
    e.preventDefault();
  });

  u("#check-pw").on("input", (e) => {
    if (e.currentTarget.value !== u("#pw").nodes.at(0).value) {
      u("#error-ch-pw").nodes.at(0).style.display = "block";
      state.ifPw = false;
    } else {
      u("#error-ch-pw").nodes.at(0).style.display = "none";
      state.ifPw = true;
    }
  });
  u("#submit-reg").on("click", () => {
    if (state.ifId && state.ifPw) {
      u(".ca-form").nodes.at(0).submit();
    }
  });
})();
