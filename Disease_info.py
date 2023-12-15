info_dict = {
    "Velvet": "Velvet disease (also called Coral disease, Gold Dust disease, or Rust disease) is a fish disease "
              "caused by small parasites in your Betta tank. These single-celled organisms penetrate a Siamese "
              "Fighting fish’s slime coat and begin to eat at its cells. It has been found in marine tanks but "
              "affects freshwater aquariums more often.",

    "Ich": "Ich or Ick is an uncomfortable disease and one of the most common among freshwater aquarium fish. Betta "
           "fish are also susceptible to ich, and ignoring treatment for too long can lead to death. When a betta "
           "fish is stressed, or living in poorly heated or poor water conditions, they are more likely to contract "
           "ich. These are the most common reasons that the Ich parasite may prey on your betta. Ich is also common "
           "among aging betta fish.",

    "Popeye": "Most of the time, Popeye is simply a bacterial infection of the eye. A betta is not at all likely to "
              "contract it if it’s kept in a clean aquarium. An aquarium with inadequate water conditions is usually "
              "the cause Popeye, in most cases but not all. Popeye isn’t difficult to cure, but it can sometimes be "
              "an indication that your betta has a serious internal condition. If that’s the case, then Popeye may "
              "prove fatal for your betta. Popeye is incurable if it’s a sign of a serious internal disease.",

    "Fin Rot": "Betta fin rot and tail rot (melt) is a gram-negative bacterial infection or fungal infection that is "
               "extremely prevalent in betta fish. More common in uncycled tanks and small bowls, fin rot attacks and "
               "begins to eat away at a betta fish’s beautiful fins. Many bettas purchased from large box stores may "
               "already show signs of fin rot due to water quality and temperature problems in small cups. Be careful "
               "not to confuse fin rot with fin biting, tearing, or splitting. These are due to physical injury from "
               "boredom, fighting, or snagging sharp decor. You don’t want to medicate an otherwise healthy fish. The "
               "major difference here is the lack of white, red or black edges around the deterioration.",

    "Columnaris": "Columnaris goes by several different names, including cotton wool disease, cotton mouth disease, "
                  "and saddleback disease, and it is a fairly common condition among freshwater aquarium fish. "
                  "Despite its cotton-wool, “fungal-like” appearance, columnaris is not caused by a fungus, "
                  "but rather by a bacterium called Flavobacterium columnare. It can affect all species of fish in a "
                  "freshwater tank, not just Bettas, so you’ll want to get rid of it as soon as it appears. "
                  "Unfortunately, it causes death rather rapidly (especially in a tropical aquarium) and death "
                  "usually occurs in 2-3 days if no treatment is attempted.",

    "Hole in the Head": "This unusual disease is believed to be a parasitic infection caused by an organism called "
                        "Hexamita. This parasite is believed to begin eating away at the flesh on and around the "
                        "head, causing deep, pitting wounds. The other name for Hole in the Head disease is "
                        "Hexamitiasis and it seems to be most common in various types of Cichlids. However, "
                        "just because Betta fish are prone to getting Hole in the Head disease doesn’t mean they are "
                        "immune from it.",

    "Dropsy": "Dropsy in betta fish is not a disease itself, but rather a secondary symptom of another problem going "
              "on internally. Think of this like when you have an infected cut, and a secondary symptom of the cut "
              "can be warm skin or swelling surrounding the cut. The iconic symptom of dropsy is the visual bloat and "
              "swelling of the stomach which causes a betta’s scales to flare out and present a pinecone appearance. "
              "This is different than overfeeding and constipation bloat. Dropsy is easily identified by looking down "
              "on your betta from above. Other symptoms include virtually non-existent appetites, extreme lethargy, "
              "darting to the surface and gasping for air, and color loss.",

    "Swim Bladder Disorder": "Swim bladder disease is a condition that occurs when a fish's swim bladder isn't "
                             "working properly. The swim bladder is a gas-filled internal organ that helps bony fish "
                             "maintain buoyancy. The disorder refers to a collection of issues affecting the swim "
                             "bladder, rather than a single disease. Although commonly seen in goldfish and bettas, "
                             "swim bladder disease can affect virtually any species of fish. The disorder is often "
                             "treatable, and a fish can experience a full recovery.",

    "Constipation": "Constipation in betta fish is a common ailment that can have negative effects on their health. "
                    "The main causes of constipation in bettas include a poor diet, overfeeding, lack of exercise, "
                    "and not enough fiber in their food. To treat constipation, you can fast your betta for 2-3 days, "
                    "feed them a boiled pea or daphnia, and consider using Epsom salt in a quarantine tank."
}

questions = [
            {"question": "1: Do you see a gold, pollen-like substance on your betta when you shine a light on them?" ,
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "2: Does your betta have white spots on it?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "3. Does your betta seem lethargic or more inactive than usual?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "4. Does your betta seem to have a swollen abdomen?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "5. Does your betta seem to have trouble swimming?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "6. Do your betta's eyes seem to be popping out?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "7. Do your betta's fins seems to look weathered?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "8. Does your betta have clamped fins?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "9. Take a look at your betta's head. Do you see something similar to a hole in the area?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "10. Is your betta trying to scratch against surfaces?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "11. Does your betta refuse to eat?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "12. Does your betta seem to have trouble breathing. Do you see it gasping?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "13. Do you see cottony patches on your betta?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "14: Are your betta's scales flaking off?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "15: Is your betta 'pineconing' aka puffing out like a pufferfish?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "16: Does you betta appear to be floating at the top of the tank or on the bettas side?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
            {"question": "17. Does your betta's feces appear to be pale and stringy?",
             "choices": ["Yes", "No", "Previous Question", "Restart Quiz"]
             },
        ]

answers = {1: ["Velvet"],
                         2: ["Ich"],
                         3: ["Velvet", "Ich", "Popeye", "Hole in \nthe Head", "Dropsy", "Constipation"],
                         4: ["Swim Bladder \nDisorder", "Constipation"],
                         5: ["Swim Bladder \nDisorder", "Constipation"],
                         6: ["Popeye"],
                         7: ["Fin Rot", "Velvet", "Columnaris"],
                         8: ["Velvet", "Ich"],
                         9: ["Hole in \nthe Head"],
                         10: ["Velvet", "Ich", "Columnaris"],
                         11: ["Ich", "Velvet", "Popeye", "Hole in \nthe Head", "Dropsy", "Constipation"],
                         12: ["Ich", "Velvet", "Columnaris", "Dropsy"],
                         13: ["Columnaris"],
                         14: ["Columnaris", "Velvet"],
                         15: ["Dropsy"],
                         16: ["Swim Bladder \nDisorder"],
                         17: ["Constipation"]}
