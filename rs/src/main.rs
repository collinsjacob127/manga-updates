use std::collections::HashMap;
use std::time::Duration;
use reqwest::Client;
use reqwest::Response;
use select::document::Document;
use select::predicate::Name;

extern crate reqwest;
extern crate select;
extern crate serde_json;
extern crate tokio;

async fn get_response(client: &Client, url: &str) -> Result<Response, reqwest::Error> {
    let response = client
        .get(url)
        .timeout(Duration::new(2, 0))
        .send()
        .await?;
    Ok(response)
}

#[tokio::main]
async fn main() {
    let mut library: HashMap<String, (String, String)> = HashMap::new();
    let urls = vec![
        "https://www.example1.com/manga/chapter1",
        "https://www.example2.com/comic/issue1",
        "https://www.example3.com/novel/volume1",
    ];

    let tag_map: HashMap<&str, (&str, &str)> = [
        ("www.example1.com", ("div.current-chapter", "span.last-updated")),
        ("www.example2.com", ("h1.current-issue", "span.last-updated")),
        ("www.example3.com", ("h1.current-volume", "span.last-updated")),
    ].iter().cloned().collect();

    let client = Client::new();

    for url in urls {
        let response: Result<Response, reqwest::Error> = get_response(&client, url).await;


        match response {
            Ok(response) => {
                if response.status().is_redirection() {
                    let redirect_url = response.url();
                    let response = get_response(&client, redirect_url.as_str()).await.unwrap();

                    let bytes = response.bytes().await.unwrap();
                    let cursor = std::io::Cursor::new(bytes);
                    let document = Document::from_read(cursor).unwrap();

                    let domain = redirect_url.domain().unwrap();
                    let tags = tag_map.get(domain).unwrap();

                    let current_chapter = document.find(Name(tags.0)).next().unwrap().text().collect::<Vec<_>>().join("");
                    let last_updated = document.find(Name(tags.1)).next().unwrap().text().collect::<Vec<_>>().join("");

                    // let current_chapter = document.find(Name(tags.0)).next().unwrap().text();
                    // let last_updated = document.find(Name(tags.1)).next().unwrap().text();

                    let entry = library.entry(redirect_url.to_string()).or_insert((current_chapter, last_updated));
                    if entry.0 != current_chapter || entry.1 != last_updated {
                        println!("There is a new update for {}", redirect_url);
                        *entry = (current_chapter, last_updated);
                    }
                }
            }
            Err(err) => {
                println!("Error making request to {}: {}", url, err);
            }
        }
    }

    let json_string = serde_json::to_string(&library).unwrap();
    std::fs::write("library.json", json_string).unwrap();
}