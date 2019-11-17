import csv , os, glob , random, time , codecs
import pandas as pd
import requests, urllib
from bs4 import BeautifulSoup

# the functions which could garb only the plot and intro
def plot_text(soup):
    start = soup.find('h2').find_next('p')
    plot = start.text.strip()
    for elem in start.next_siblings:
        if elem.name != 'p':
            break
        plot += elem.text.strip()
    return plot

def intro_text(soup):
    start = soup.find('p')
    intro = start.text.strip()
    for elem in start.next_siblings:
        if elem.name != 'p':
            break
        intro += elem.text.strip()
    return intro
    
