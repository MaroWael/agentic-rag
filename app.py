import asyncio

from agents import Runner

from agent import study_agent


async def main():

    result = await Runner.run(
        study_agent,
        input="What is Reinforcement Learning?"
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())