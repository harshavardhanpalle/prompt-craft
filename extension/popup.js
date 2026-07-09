const optimizeButton = document.getElementById(
    "optimizeBtn"
);


const promptInput = document.getElementById(
    "promptInput"
);


const resultBox = document.getElementById(
    "result"
);


const loading = document.getElementById(
    "loading"
);


const stats = document.getElementById(
    "stats"
);



optimizeButton.addEventListener(
    "click",
    async () => {


        const prompt = promptInput.value.trim();


        if (!prompt) {

            alert("Please enter a prompt");

            return;

        }


        loading.classList.remove("hidden");


        resultBox.value = "";


        try {


            const response = await fetch(
                "http://localhost:8000/api/optimize",
                {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json"

                    },


                    body: JSON.stringify({

                        prompt: prompt

                    })

                }
            );



            if (!response.ok) {

                throw new Error(
                    "API request failed"
                );

            }



            const data = await response.json();



            resultBox.value =
                data.optimized_prompt;



            stats.innerHTML =
                `
                Original words: ${data.original_length}
                <br>
                Optimized words: ${data.optimized_length}
                <br>
                Reduction: ${data.token_reduction_percentage}%
                `;



        } catch(error) {


            resultBox.value =
                "Error connecting to backend";


            console.error(error);


        } finally {


            loading.classList.add(
                "hidden"
            );

        }


    }
);