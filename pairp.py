import argparse
import os
import sys
import google.generativeai as palm

API_KEY = "GOOGLE_GENERATIVE_AI_API_KEY"

def get_model_bison():
    apikey = os.getenv(API_KEY)
    if not apikey:
        print(f"must set environment variable {API_KEY}")
        exit(0)
    palm.configure(api_key=apikey, transport="rest")
    models = [m for m in palm.list_models() if "generateText" in m.supported_generation_methods]
    if not len(models):
        print("no model support method generateText, why?")
        exit(0)
    return models[0]
    

def generate_text(prompt, model, temperature=0.8):
    return palm.generate_text(prompt=prompt, 
                              model=model, 
                              temperature=temperature)



def main():
    parser = argparse.ArgumentParser(prog="pairp", usage="%(prog)s [options]", 
                                     description="pairp is a good pair programmer",
                                     epilog="version v1.0.0")
    parser.add_argument("-p", "--prompt", help="full prompt used in LLM")

    args = parser.parse_args()

    if "--help" in sys.argv:
        args.print_help()
        exit(0)

    prompt = args.prompt
    model_bison = get_model_bison()
    complet = generate_text(prompt, model=model_bison)
    print(complet.result)
    


if __name__ == "__main__":    
    main()
